#!/usr/bin/perl
die $! if($#ARGV<0);
$opt=shift or die $!;
$file1=shift or die $!;
$file2="";
$file2=shift or die $! if($#ARGV>=0);
die $! if($#ARGV>=0);

if($opt eq "-w")
{
    $output=qx{wc -w $file1};
    print "Numero di parole: $output";
}
elsif($opt eq "-d")
{
    if($file2 ne ""){
        @output=qx{diff $file1 $file2};
        print "@output";
    }
    else
    {
        print "file2 non presente\n";
    }
}
elsif($opt eq "-s")
{
    if($file2 ne ""){
        $sorted=qx{sort $file1};
        open($fh,">",$file2) or die $!;
        print $fh "$sorted";
        close $fh;
    }
    else
    {
        print "file2 non presente\n";
    }
}
else {
    print "Parametro errato\n";
}