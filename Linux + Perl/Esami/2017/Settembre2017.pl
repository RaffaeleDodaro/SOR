#!/usr/bin/perl
@output=qx(cat /proc/meminfo);
$time = 2;
$time = shift or die $! if ($#ARGV>=0);
die $! if ($#ARGV>=0);
$memfreeVecchia=0;
$conto=0;
$diff;
@tutteDiff;
while(True){
    if($conto==5)
    {
        $conto=0;
        open($fh,">>","mem_free.log") or die $!;
        $pos="";
        $neg="";
        foreach(@tutteDiff)
        {
            $pos = $pos."$_, " if($_> 0);
            $neg = $neg."$_, " if($_< 0);
            # all'ultimo elemento di @tuttediff non ci dovrebbe andare la ,
            # ma con con questo codice ci va (i'm lazy!!)
        }
        print $fh "i\n$pos\nd\n$neg\n----------\n";
        close $fh or die $!;
        @tutteDiff=();
    }

    @output=qx(cat /proc/meminfo);
    foreach(@output)
    {
        if(m/MemFree:\s+(\d+)\s+kB/)
        {
            $diff=$1-$memfreeVecchia;
            $memfreeVecchia=$1;
            print "< $diff kB\n" if($diff < 0);
            print "> $diff kB\n" if($diff > 0);
            print "= $diff kB\n" if($diff == 0);
            push @tutteDiff, $diff;
        }
    }
    $conto+=1;
    sleep($time);
}