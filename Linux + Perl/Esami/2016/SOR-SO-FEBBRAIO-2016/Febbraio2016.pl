#!/usr/bin/perl
die $! if($#ARGV ne 0);
$parametro=shift or die$!;
foreach(qx{ls ./rss})
{
    $nomeFile=$1 if(m/(\N+)/);
    open(my $fh,"<","./rss/$nomeFile") or die $!;
    $nomeNotizia="-1";
    while(<$fh>)
    {
        $nomeNotizia=$1 if(m/<title><\!\[CDATA\[(.+$parametro.+)\]\]/);

        if($nomeNotizia ne "-1" and $_ =~ m/<link>(.+)<\/link>/)
        {
            open($fh2,">>","output.txt") or die $!;
            print $fh2 "$nomeNotizia --> $1\n\n";
            close $fh2 or die $!;
            $nomeNotizia="-1";
        }
    }
    close $fh or die $!;
}