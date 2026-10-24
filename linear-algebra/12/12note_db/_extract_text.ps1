$bytes = [System.IO.File]::ReadAllBytes("D:\Note\linear-algebra\12\la-12\assignment.one")
$text = [System.Text.Encoding]::Unicode.GetString($bytes)
# Match runs of printable chars including Chinese, digits, math symbols
$pattern = '[一-鿿　-〿＀-￯a-zA-Z0-9\s\.\,\(\)\[\]\{\}\+\-\=\/\:\;\<\>\!\?\^\|\*\&\%\$\#@~_°λ∈ℝ→↔⊕⊗∑∏√αβγδεζηθικλμνξοπρστυφχψωΔΣΠΦΨΩ]{4,}'
$matches = [regex]::Matches($text, $pattern)
$seen = @{}
$out = New-Object System.Collections.Generic.List[string]
foreach ($m in $matches) {
    $v = $m.Value.Trim()
    # filter out runs that are mostly garbage (random repeated chars)
    if ($v.Length -lt 4) { continue }
    # skip strings with >30% rare CJK chars (garbage)
    $cjk = ([regex]::Matches($v, '[一-鿿]')).Count
    if ($cjk -gt 0) {
        $ratio = $cjk / $v.Length
        # allow if ratio reasonable, but skip obvious garbage (repeated same char)
        $uniq = ($v.ToCharArray() | Select-Object -Unique).Count
        if ($uniq -lt 3 -and $v.Length -gt 8) { continue }
    }
    if (-not $seen.ContainsKey($v)) {
        $seen[$v] = $true
        $out.Add($v)
    }
}
$out | ForEach-Object { Write-Output $_ }
