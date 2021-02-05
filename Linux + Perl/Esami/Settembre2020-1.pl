#!/usr/bin/perl
die "troppi argomenti" if($#ARGV>=2);
$tipo= shift or die $!;
$utente = shift or die $!;

open($fh,">","stat.log");
@output=`top -n1 -b`;
if($tipo=~m/-c|-C/)
{
    %cpu;
    for(@output)
    {
        if($_ =~ m/\d+\s+(\w+)\s+\d+\s+\d+\s+\d+\d+\s+\d+\d+\s+\d+\s+\w+\s+(\d+\.\d+)/)
        {
            $cpu{$1}+=$2;
        }
    }
    print $fh "utente $utente CPU: $cpu{$utente} %\n";
    foreach $user(sort{$cpu{$a}<=>$cpu{$b}} keys %cpu)
    {
        print $fh "utente $user CPU: $cpu{$user} %";
        last;
    }
}
elsif($tipo=~m/-m|-M/)
{
    %memoria;
    for(@output)
    {
        if($_ =~ m/\d+\s+(\w+)\s+\d+\s+\d+\s+\d+\d+\s+\d+\d+\s+\d+\s+\w+\s+(\d+\.\d+)/)
        {
            $memoria{$1}+=$2;
        }
    }
    print $fh "utente $utente Memoria: $memoria{$utente} %\n";
    foreach $user(sort{$memoria{$a}<=>$memoria{$b}} keys %memoria)
    {
        print $fh "utente $user CPU: $memoria{$user} %";
        last;
    }
}
close $fh;