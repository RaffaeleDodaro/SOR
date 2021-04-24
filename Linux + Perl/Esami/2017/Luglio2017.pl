#!/usr/bin/perl
$utente=qx{whoami};
$utente = shift or die $! if($#ARGV>=0);
die $! if($#ARGV>=0);
$utente=$1 if($utente =~m/(\N+)/);
@output=qx{lsof};
$hash;
foreach(@output)
{
    $hash{$1}.="\n:$2:$3\n" if(m/bash\s+(\d+)\s+$utente\s+\S+\s+(\w+)\s+\d+\,\d+\s+\d+\s+\d+\s+(\N+)/)
}
foreach(keys %hash)
{
    print "$_ $hash{$_}";
}