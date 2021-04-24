#!/usr/bin/perl
die $! if($#ARGV<0 or $#ARGV >1);
$nome=shift or die $!;
$intervallo=shift or die $!;
$vecchio=-1;
while(True)
{
    foreach(qx{df})
    {
        if(m/$nome\s+\d+\s+(\d+)/)
        {   
            if($vecchio ne $1)
            {
                print $_;
                $vecchio=$1;
            }
        }
    }
    sleep $intervallo;
}