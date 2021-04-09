#!/usr/bin/perl
$somma=0;
foreach(`ps -elf`)
{
    if(m/(?i)chrome/)
    {
        if(m/\d+\s+\w+\s+\w+\s+(\d+).+/)
        {
            open($fh,"<","/proc/$1/status");
            while(<$fh>){
                if(m/VmRSS\:\s+(\d+).+/)
                {
                    $somma+=$1;
                }
            }
            close $fh;
        }
    }
}
print"somma: $somma\n";