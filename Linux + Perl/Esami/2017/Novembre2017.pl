#!/usr/bin/perl
$par="-c";

@output=qx(top -n 1 -b | tail -n +7);
$par = shift or die $! if($#ARGV>=0);
die $! if($#ARGV>=0);
%hash;
if($par =~m/-c/)
{
    foreach(@output)
    {
        if(m/\d+\s+(\S+)\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\w+\s+(\S+).+/)
        {
            $hash{$1}+=$2;
        }
    }
    open($fh,">","top_stat.log") or die $!;
    print "USER -- %CPU\n";
    print $fh "USER -- %CPU\n";
    foreach(sort{$hash{$b}<=> $hash{$a} or $a cmp $b} keys %hash)
    {
        print "$_ -- $hash{$_}%\n";
        print $fh "$_ -- $hash{$_}%\n";
    }
    close $fh or die $!;
}
elsif($par =~m/-m/)
{
    foreach(@output)
    {
        if(m/\d+\s+(\S+)\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\w+\s+\S+\s+(\S+).+/)
        {
            $hash{$1}+=$2;
        }
    }
    open($fh,">>","top_stat.log") or die $!;
    
    print "USER -- %MEM\n";
    print $fh "USER -- %MEM\n";
    foreach(sort{$hash{$b}<=> $hash{$a} or $a cmp $b} keys %hash)
    {
        print "$_ -- $hash{$_}%\n";
        print $fh "$_ -- $hash{$_}%\n";
    }
    print $fh "####################\n";
    close $fh or die $!;
}
else{
    die $!;
}
