#!/usr/bin/perl
die $! if($#ARGV<0);
$option = shift or die $!;
open(my $fh,">>","file_history.txt") or die $!;

if($option eq "-t")
{
    die $! if($#ARGV<0);
    $file=shift or die $!;
    $stringa;
    if($#ARGV>=0)
    {
        $stringa=shift or die $!;
    }
    else
    {
        print "Inserire le parole da tradurre separate da virgola (,)";
        $stringa=<STDIN>;
    }
    @parole=split(',',$stringa);
    
    while(@parole)
    {
        print $fh $_;
        print "La traduzione di $_ e': "
    }
}
elsif($option eq "-h")
{
    foreach($fh)
    {
        print "$_\n";
    }
}
else 
{
    die "param not accepted";
}
close $fh;