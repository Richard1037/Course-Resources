$bytes = [System.IO.File]::ReadAllBytes("D:\Note\linear-algebra\12\la-12\assignment.one")
Write-Output ("Size: " + $bytes.Length)
$text = [System.Text.Encoding]::Unicode.GetString($bytes)
$pattern = '[\u4e00-\u9fff\u3000-\u303f\uff00-\uffefa-zA-Z0-9\s\.\,\(\)\[\]\{\}\+\-\=\/\:\;\<\>\!\?\^\|\*\&\%\$\#@~_]{6,}'
$matches = [regex]::Matches($text, $pattern)
$i = 0
foreach ($m in $matches) {
    $v = $m.Value.Trim()
    if ($v.Length -ge 6) {
        Write-Output ("---[" + $i + "]---")
        Write-Output $v
        $i++
        if ($i -ge 200) { break }
    }
}
