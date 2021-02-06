#!/usr/bin/perl
@output=`ps -elf`;
$somma=0;
foreach(@output)
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