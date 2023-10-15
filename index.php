<?php
function saveSha1($data)
{
  $sha1 = "sha1.enc";
  if ($sha1_open = fopen($sha1, "a")) {
    fwrite($sha1_open, $data . PHP_EOL);
    return true;
  } else {
    echo "Unable to open $sha1_open for writing.";
  }
}

$numbers = "numbers.txt";
if (file_exists($numbers)) {
  $file = fopen($numbers, "r");
  while (!feof($file)) {
    $line = fgets($file);
    saveSha1(sha1($line));
  }
  echo "  File Saved Successfully!";
  fclose($file);
} else {
  echo "The file $numbers does not exist.";
}

?>
