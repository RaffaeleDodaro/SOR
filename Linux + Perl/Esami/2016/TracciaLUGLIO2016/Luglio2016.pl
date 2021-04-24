#!/usr/bin/perl
die $! if($#ARGV!=0);
$path=shift or die $!;
open($fh,"<",$path) or die $!;
    
while(<$fh>)
{ 
    if(m/(\d+\.\d+\.\d+\.\d+).+\"\w+\s(\S+).+"\s(\d+)/)
    {
        open($stato_status,">>","stato_$3")or die $!;
        print $stato_status "$1 : $2\n";
        close $stato_status or die $!;
    }
}
close $fh;