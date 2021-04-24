#!/usr/bin/perl
die $! if($#ARGV<0 or $#ARGV>2);
$user =qx{whoami};
$user=$1 if($user =~ m/(\N+)/);
$user=shift or die $! if($#ARGV==2);
$option=shift or die $!;
$path=shift or die $!;
open($fh,"<",$path)or die $!;
@array;
if($option =~m/-t=\"?(\S+)\"?/)
{
    while(<$fh>)
    {
        push @array, $_ if(m/\d+\.\d+\s\d+\:\d+\:\d+\s$user\s$1.+/);
    }
}
elsif($option =~m/-hw/)
{
    while(<$fh>)
    {
        push @array, $_ if(m/(?i) memory | dma | usb | tty /);
    }
}
else{die $!;}
close $fh or die $!;
$date=qx{date "+%Y-%m-%d"};
$date=$1 if($date=~m/(\d+\-\d+\-\d+)/);
open($fh,">",$date)or die $!;
print $fh reverse @array;
close $fh or die $!;