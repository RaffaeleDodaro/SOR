#!/usr/bin/perl
$valore=<STDIN>;
@tantiValori;
while ($valore ne "-1") {
    push @tantiValori, $valore;
    $valore=<STDIN>;
}
%nomeVmRSS;
foreach(@tantiValori)
{
    chomp;
    open(my $fh,"<","/proc/$_/status") or die $!;
    $nome="";
    while(my $line=<$fh>)
    {
        if($line =~m/(?i)Name:\s+(\S+)\n/)
        {
            $nome=$1;
        }
        if($line =~m/(?i)VmRSS:\s+(\d+)/)
        {
            $nomeVmRSS{$nome}=$1;
        }
    }
    
    close $fh;
}
@sorted=sort{$nomeVmRSS{$b}<=> $nomeVmRSS{$a} or $a cmp $b} keys %nomeVmRSS;
foreach(@sorted)
{
    print "$_ --> $nomeVmRSS{$_}";
}
qx(top -n1);