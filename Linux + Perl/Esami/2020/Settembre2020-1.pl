#!/usr/bin/perl
die $! if($#ARGV>1 or $#ARGV<0);
$tipo= shift or die $!;
$utente = shift or die $!;
open($fh,">","stat.log") or die $!;
%array;
if($tipo=~m/(?i)-c/)
{
    for(`top -n1 -b`)
    {
        $array{$1}+=$2 if($_ =~ m/\d+\s+(\w+).+\s+(\d+\,\d+)\s+(\d+\,\d+)/);
    }
    print $fh "utente $utente CPU: $array{$utente}%\n";
    foreach $user(sort{$array{$b}<=>$array{$a}} keys %array)
    {
        print $fh "utente $user CPU: $array{$user}%\n";
        last;
    }
}
elsif($tipo=~m/(?i)-m/)
{
    for(`top -n1 -b`)
    {
        $array{$1}+=$2 if($_ =~ m/\d+\s+(\w+).+\s+\d+\,\d+\s+(\d+\,\d+)/);
    }
    print $fh "utente $utente Mem: $array{$utente}%\n";
    foreach $user(sort{$array{$b}<=>$array{$a}} keys %array)
    {
        print $fh "utente $user Mem: $array{$user}%\n";
        last;
    }
}
else {die $!;}
close $fh or die $!;