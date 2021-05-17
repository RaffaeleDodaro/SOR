#!/usr/bin/perl
die $! if ($#ARGV < 0 or $#ARGV > 1);
$name = shift or die $!;
$conto=0;
$str="";
foreach(qx{cat ~/.bash_history | nl})
{
    if(m/\d+\s+$name\s+(\N+)/)
    {
        $conto +=1;
        $str=$str."       $1\n";
    }
}
print "$name $conto\n$str";