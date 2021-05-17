#!/usr/bin/perl
die $! if($#ARGV<0 or $#ARGV>1);
$risorsa = shift or die $!;
$utente=shift or die $!;
%hash;
foreach(qx{top -n1 -b})
{
    if(m/\d+\s(\S+).+\w\s+(\d+\.\d)\s+(\d+\.\d)\s/){
        $u=$1;
        $c=$2;
        $m=$3;
        if($risorsa eq "-c")
        {            $hash{$1}+=$2;        }
        elsif($risorsa =~m/-m/)
        {            $hash{$1}+=$3         }
        else{die$!;}
    }
}
open($fh,">","stat.log") or die $!;
foreach(sort{$hash{$b}<=>$hash{$a}} keys %hash)
{
    print $fh "$utente --> $hash{$utente}\n$_ --> $hash{$_}\n";
    last;
}
close $fh or die $!;