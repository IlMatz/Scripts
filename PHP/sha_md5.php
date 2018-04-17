<?php
// USAGE EXAMPLE
// zcat /usr/share/wordlists/rockyou.txt.gz | php sha_md5.php > rockyou_sha_md5.txt

while($f = fgets (STDIN){
	$passwenc = md5(sha1(rtrim($f)));
	echo "$passwenc : $f";
}
?>
