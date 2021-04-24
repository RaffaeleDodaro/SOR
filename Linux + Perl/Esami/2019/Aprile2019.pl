#!/usr/bin/perl
die $! if($#ARGV<0 or $# $#ARGV>1);
$boolkill=shift or die $!;
$boolkill=$1 if($kill ~= m/--kill=(\w+)/);
die $! if($kill ne "true" and $kill ne "false");
$nameProcess=shift or die $!;
$nameProcess=$1 if($name ~= m/--name=(\S+)/);
@output=qx(ps aux);
$tantipid;
die $! if ($boolkill eq "true" and $nameProcess eq "ALL");
if($boolkill eq "true")
{
    @pid;
    foreach(@output)
    {
        $tutta=$_;
        if(m/\S+\s+(\d+).+\d+\:\d+\s+\d+\:\d+\s+(\S+)/)
        {
            $f=$2;
            $pid=$1;
            if($f=~m/(?i)$nameProcess/)
            {
                print "$tutta\n";
                $tantipid=$tantipid.$p." ";
            }
        }
    }
    qx{kill $tantipid};
}
elsif($boolkill eq "false" and $nameProcess eq "ALL")
{
    print "@output";
}
elsif($boolkill eq "false")
{
    $cpu=0.0;
    $mem=0.0;
    foreach(@output)
    {
        if(m/\S+\s+(\S+)\s+(\S+)\s+(\S+).+\d+\:\d+\s+\d+\:\d+\s+(\S+)/)
        {
            $f=$3;
            $c=$1;
            $m=$2;
            if($f=~m/(?i)$nameProcess/)
            {
                $cpu+=$c;
                $mem+=$m;
            }
        }
    }
    print "cpu: $cpu\n mem: $mem\n";
}