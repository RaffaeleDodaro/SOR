#!/usr/bin/perl
$par=shift or die $!;
$tempo=shift or die $!;
$iterazioni=shift or die $!;
$i=0;
open($fh,">","stats.log")or die $!;
$max=0;
while($i<$iterazioni)
{
    if($par =~m/all/)
    {
        @output_cpu=qx(cat /proc/cpuinfo);
        %cpu;
        foreach(@output_cpu)
        {
            $nome;
            $nome=$1 if(m/processor\s+\:\s+(\d+)/);
            print"CPU: $nome --> $1\n" if(m/cpu MHz\s+\:\s+(\S+)/);
        }

        @output_mem=qx(cat /proc/meminfo);
        %cpu;
        foreach(@output_mem)
        {
            if(m/MemFree:\s+(\d+)\skB/)
            {
                print"Memfree: $1\n";
                $max=$1 if($1>$max);
            }
        }
    }
    elsif($par =~m/cpu/)
    {
        @output_cpu=qx(cat /proc/cpuinfo);
        %cpu;
        foreach(@output_cpu)
        {
            $nome;
            $nome=$1 if(m/processor\s+\:\s+(\d+)/);
            print"CPU: $nome --> $1\n" if(m/cpu MHz\s+\:\s+(\S+)/);
        }
    }
    elsif($par =~m/mem/)
    {
        @output_mem=qx(cat /proc/meminfo);
        %cpu;
        foreach(@output_mem)
        {
            if(m/MemFree:\s+(\d+)\skB/)
            {
                print"Memfree: $1\n";
                $max=$1 if($1>$max);
            }
        }
    }
    sleep($tempo);
    print `reset`;
    $i+=1;
}

print $fh "Max mem: $max\n";
close $fh;