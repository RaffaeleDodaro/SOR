#!/usr/bin/perl
$file= shift or die $!;
$ip=shift or die $!;
$porta=shift or die $!;
die $! if($#ARGV>=0);
open(my $fh,"<",$file) or die $!;
$conto=0;
%array;
while(<$fh>)
{
    if(m/IP\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).(\d+)\s>\s$ip\.$porta/)
    {
        $array{$1}+=1
    }
}
close $fh;
open(my $fh,">","output.log") or die $!;
my @sorted= sort{$array{$b}<=>$array{$a} }keys %array;
foreach(@sorted)
{
    print $fh "$_>$ip.$porta --> $array{$_}\n";
}
close $fh;