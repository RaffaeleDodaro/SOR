#!/usr/bin/perl
die $! if($#ARGV > 0 or $#ARGV<0);
$par = shift or "-c" if($#ARGV >= 0);
%hash;
foreach(qx{top -n 1 -b | tail -n +7})
{
    if($par eq "-c")
    {
        $hash{$1}+=$2 if(m/\d+\s+(\S+)\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\w\s+(\d+\,\d+)\s+(\d+\,\d+)\s+/)
    }
    elsif($par eq "-m")
    {
        $hash{$1}+=$3 if(m/\d+\s+(\S+)\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\w\s+(\d+\,\d+)\s+(\d+\,\d+)\s+/);
    }
    else{die $!;}
}
open(my $fh,">>","top_stat.log") or die $!;
print "USER --- \%CPU\n" if($par eq "-c");
print $fh "USER --- \%CPU\n" if($par eq "-c");
print "USER --- \%MEM\n" if($par eq "-m");
print $fh "USER --- \%MEM\n" if($par eq "-m");
foreach(sort{$hash{$b}<=>$hash{$a}}keys %hash)
{
    print "$_ --- $hash{$_}\%\n";
    print $fh "$_ --- $hash{$_}\%\n";
}
print $fh "####################";
close $fh;