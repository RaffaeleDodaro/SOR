#!/usr/bin/perl
$somma=0;
foreach(`ps -elf`)
{
    if(m/(?i)chrome/)
    {
        if(m/\d+\s+\w+\s+\w+\s+(\d+).+/)
        {
            open($fh,"<","/proc/$1/status")or die $!;
            while(<$fh>){
                $somma+=$1 if(m/VmRSS\:\s+(\d+).+/);
            }
            close $fh or die $!;
        }
    }
}
print"somma: $somma\n";