#!/usr/bin/perl
die $! if($#ARGV<0 or $#ARGV >1);
$nome=shift or die $!;
$intervallo=shift or die $!;
$vecchio=-1;
while(True)
{
    @output=qx{df};
    
    foreach(@output)
    {
        if(m/$nome\s+\d+\s+(\d+)/)
        {   
            if($vecchio!=$1)
            {
                print $_;
                $vecchio=$1;
            }
        }
    }
    sleep $intervallo;
}