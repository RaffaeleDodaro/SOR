#!/usr/bin/perl
die $! if($#ARGV<0 or $#ARGV>2);
$user=qx{whoami};
$user=$1 if($user=~m/(\N+)/);
$user= shift or die $! if($#ARGV==2);
$options=shift or die $!;
$path=shift or die $!;
open($fh,"<",$path) or die $!;
@output;

if($options =~m/-t=\"?(\w+)\"?/)
{
    $tipo=$1;
    
    while(<$fh>)
    {
        push @output, $_ if(m/.+\:\d+\s+$user\s$tipo/);
    }
}
elsif($options =~m/-hw/)
{
    while(<$fh>)
    {
        push @output, $_ if(m/\d+\.\d+\s\d+\:\d+\:\d+\s\S+\s\S+\:\s(?i)memory|dma|usb|tty/);
    }
}
else {
    die $!;
}
close $fh or die $!;

$data=qx{date "+%Y-%m-%d"};
$data=$1 if($data=~m/(\N+)/);
open($fh,">",$data) or die $!;
@reversed = reverse @output;
print $fh "@reversed";
close $fh or die $!;