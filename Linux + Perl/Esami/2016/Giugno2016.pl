#!/usr/bin/perl
open($fh,"<","./TracciaGIUGNO2016/info.txt") or die $!;
qx{rm ./TracciaGIUGNO2016/info.csv};
open($fh2,">","./TracciaGIUGNO2016/info.csv") or die $!;
print $fh2 "Hostname, OS, MemoryGB, CPUcount, DiskSpace, Location\n";
while(<$fh>)
{
    $str=$str.$1."," if(m/Hostname: (\N+)/);
    $str=$str.$1."," if(m/OS: (\N+)/);
    $str=$str.$1."," if(m/MemoryGB: (\d+)/);
    $str=$str.$1."," if(m/CPUcount: (\d+)/);
    $str=$str.$1."," if(m/DiskSpace: (\N+)/);
    if(m/Location: (\N+)/){
        $str=$str.$1;
        print $fh2 "$str\n";
        $str = "";
    }
}
close $fh2 or die $!;
close $fh or die $!;