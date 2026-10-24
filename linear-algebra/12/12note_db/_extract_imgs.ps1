param()
$bytes = [System.IO.File]::ReadAllBytes("D:\Note\linear-algebra\12\la-12\assignment.one")
$outDir = "D:\Note\linear-algebra\12\12note_db\extracted_imgs"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

# PNG signature: 89 50 4E 47 0D 0A 1A 0A, IEND: 49 45 4E 44 AE 42 60 82
$sig = [byte[]](0x89,0x50,0x4E,0x47,0x0D,0x0A,0x1A,0x0A)
$end = [byte[]](0x49,0x45,0x4E,0x44,0xAE,0x42,0x60,0x82)

$positions = @()
for ($i = 0; $i -lt $bytes.Length - 8; $i++) {
    if ($bytes[$i] -eq 0x89 -and $bytes[$i+1] -eq 0x50 -and $bytes[$i+2] -eq 0x4E -and $bytes[$i+3] -eq 0x47) {
        $positions += $i
    }
}
Write-Output ("PNG starts found: " + $positions.Count)

$count = 0
foreach ($start in $positions) {
    # find IEND after start
    $endPos = -1
    for ($j = $start + 8; $j -lt $bytes.Length - 8; $j++) {
        if ($bytes[$j] -eq 0x49 -and $bytes[$j+1] -eq 0x45 -and $bytes[$j+2] -eq 0x4E -and $bytes[$j+3] -eq 0x44) {
            $endPos = $j + 8
            break
        }
    }
    if ($endPos -gt 0) {
        $len = $endPos - $start
        if ($len -gt 5000) {
            $outPath = Join-Path $outDir ("img_{0:D3}.png" -f $count)
            $slice = new-object byte[] $len
            [Array]::Copy($bytes, $start, $slice, 0, $len)
            [System.IO.File]::WriteAllBytes($outPath, $slice)
            Write-Output ("wrote " + $outPath + " size=" + $len)
            $count++
        }
    }
}
Write-Output ("Total images: " + $count)
