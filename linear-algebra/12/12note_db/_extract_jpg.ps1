$bytes = [System.IO.File]::ReadAllBytes("D:\Note\linear-algebra\12\la-12\assignment.one")
$outDir = "D:\Note\linear-algebra\12\12note_db\extracted_imgs"

# JPEG: FF D8 FF
$jpgCount = 0
for ($i = 0; $i -lt $bytes.Length - 3; $i++) {
    if ($bytes[$i] -eq 0xFF -and $bytes[$i+1] -eq 0xD8 -and $bytes[$i+2] -eq 0xFF) {
        # find FFD9
        for ($j = $i+3; $j -lt $bytes.Length - 1; $j++) {
            if ($bytes[$j] -eq 0xFF -and $bytes[$j+1] -eq 0xD9) {
                $len = $j + 2 - $i
                if ($len -gt 3000) {
                    $outPath = Join-Path $outDir ("jpg_{0:D3}.jpg" -f $jpgCount)
                    $slice = new-object byte[] $len
                    [Array]::Copy($bytes, $i, $slice, 0, $len)
                    [System.IO.File]::WriteAllBytes($outPath, $slice)
                    Write-Output ("wrote " + $outPath + " size=" + $len)
                    $jpgCount++
                }
                break
            }
        }
    }
}
Write-Output ("JPEGs: " + $jpgCount)

# Also count all PNG starts regardless of size
$pngAll = 0
for ($i = 0; $i -lt $bytes.Length - 8; $i++) {
    if ($bytes[$i] -eq 0x89 -and $bytes[$i+1] -eq 0x50 -and $bytes[$i+2] -eq 0x4E -and $bytes[$i+3] -eq 0x47) {
        $pngAll++
    }
}
Write-Output ("All PNG starts: " + $pngAll)
