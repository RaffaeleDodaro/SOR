#!/usr/bin/perl
$file=shift or die $!;
$ip=shift or die $!;
$protocollo=shift or die $!;
die "protocollo non accettato" if ($protocollo ne "UDP" && $protocollo ne "TCP");
$intero=shift or die $!;
die "troppi argomenti\n" if ($#ARGV>=0);
open(my $fh,"<",$file) or die $!;
$righe=0;
@array;
while(<$fh>)
{
    if(m/\:\s+($protocollo)/)
    {
        if(m/IP\s+($ip)./)
        {
            if(m/(\d+)\:\d+\:\d+/ && $1 eq $intero)
            {
                push @array, $_;
                $righe+=1;
            }
        }        
    }
}
close $fh;
open(my $fh,">","output.log") or die $!;
foreach(reverse @array)
{
    print $fh $_;
}
print $fh "Totale: $righe";
close $fh;