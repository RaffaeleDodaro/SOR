#!/usr/bin/perl
$par=qx(whoami);
$par=shift or die $! if($#ARGV>=0);
die $! if($#ARGV>=0);
@output=qx(lsof);
foreach(@output)
{
    if(m/bash\s+(\d+)\s+\s+$par\s+\S+\s+(\S+)\s+\S+\s+\d+\s+\d+\s+(\N+)/)
    {
        $type=$2;
        $name=$3;
        $pid=$1;
        print "$pid\n:$type:$name\n";
    }
}