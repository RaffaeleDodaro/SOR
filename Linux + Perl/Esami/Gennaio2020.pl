#!/usr/bin/perl
die "sono piu' di 3 parametri" if ($#ARGV>2);

$primoParametro=shift or die "manca il primo parametro";
$secondoParametro=shift or die "manca il secondo parametro";
$terzoParametro=shift or die "manca il percorso";
if($primoParametro=~m/-/)
{
    $user=qx(whoami);
}
#print "$primoParametro $secondoParametro $terzoParametro\n";

open(my $fh,"<",$terzoParametro) or die "non posso aprire il file $!";
@output;



while (my $line=<$fh>)
{
    #chomp $line;
    #print $line;
    #\d+.\d+\s\d+:\d+:\d+\s([a-zA-Z]+)
    if($line=~m/\d+.\d+\s\d+:\d+:\d+\s($primoParametro)/)
    {
        push @output,($line);
        #print @output;
    }
}
close $fh;
@tipoSubstr=split(/=/,$secondoParametro);



if("-t" eq @tipoSubstr[0])
{
    $tipo=@tipoSubstr[1];
    while (@output)
    {
        my $linew = shift @output;
        if($linew=~m/\d+.\d+\s\d+:\d+:\d+\s($primoParametro)\s($tipo)/)
        {
            #push @output,($line);
            print  $linew;
        }
    }
}
elsif ("-hw" eq @tipoSubstr[0]) {
    while (@output)
    {
        my $linew = shift @output;
        if($linew=~m/TTY|tty|memory|MEMORY|dma|DMA|usb|USB/)
        {
            #push @output,($line);
            print $linew;
        }
    }
}



$date=qx(date "+%Y-%m-%d");
open(my <$fh>,">>",$date)