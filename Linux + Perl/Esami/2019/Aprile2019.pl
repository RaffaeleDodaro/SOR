#!/usr/bin/perl
$kill=shift or die $!;
$name=shift or die $!;
$boolkill;
$nameProcess;
@output=qx(ps aux);
$boolkill=$1 if($kill =~ m/--kill=(\w+)/);
$nameProcess=$1 if($name =~ m/--name=(\w+)/);

die $! if ($boolkill eq "true" and $nameProcess eq "ALL");
elsif($boolkill eq "true" and $nameProcess eq "process_name")
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
                push @pid, $pid;
            }
        }
    }
    foreach(@pid)
    {
        qx(kill $_);
    }
}
elsif($boolkill eq "false" and $nameProcess eq "ALL")
{
    print "@output";
}
elsif($boolkill eq "false" and $nameProcess eq "process_name")
{
    @pid;
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