#!/usr/bin/perl

$option = shift or die "$!";
$folder = shift or die "$!" if ($option eq "--sync");
$filename = $option if ($option ne "--sync");
die "$!" if($#ARGV >= 0);

if ($option eq "--sync") {
    @file_list = `ls -aR $folder`;
    if (-e "database.db") { #se esiste il file lo apro
        open($fh, "<", "database.db") or die "$!";
        @arrayFile = <$fh>;# mi copio il contenuto attuale
        close $fh;
    }
    open($fh, ">", "database.db") or die "$!";
    foreach (@arrayFile) {
        print $fh $_ unless (m/$folder/);
    }
    foreach (@file_list) {
        chomp;
        if (m/^($folder.*)\s*:/) {
            $location = $1;
            next;
        }
        print $fh "$location --> $_\n" if (m/[^\.]/);
    }
    close $fh;
}
else {
    open($fh, "<", "database.db") or die "$!";
    
    while (<$fh>) {
        print "$1/$2\n" if (m/(.*)\s-->\s($filename.*)/);
    }
    close $fh;
}