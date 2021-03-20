#!/usr/bin/perl
die "troppi argomenti" if($#ARGV>=2);
$tipo= shift or die $!;
$utente = shift or die $!;
open($fh,">","stat.log");
@output=`top -n1 -b`;
%array;
if($tipo=~m/-c|-C/)
{
    for(@output)
    {
        if($_ =~ m/\d+\s+(\w+).+\s+(\d+\,\d+)\s+(\d+\,\d+)/)
        {
            $array{$1}+=$2;
        }
    }
    print $fh "utente $utente CPU: $array{$utente}%\n";
    foreach $user(sort{$array{$b}<=>$array{$a}} keys %array)
    {
        print $fh "utente $user CPU: $array{$user}%\n";
        last;
    }
}
elsif($tipo=~m/-m|-M/)
{
    for(@output)
    {
        if($_ =~ m/\d+\s+(\w+).+\s+\d+\,\d+\s+(\d+\,\d+)/)
        {
            $array{$1}+=$2;
        }
    }
    print $fh "utente $utente Mem: $array{$utente}%\n";
    foreach $user(sort{$array{$b}<=>$array{$a}} keys %array)
    {
        print $fh "utente $user Mem: $array{$user}%\n";
        last;
    }
}
else {die $!;}
close $fh;