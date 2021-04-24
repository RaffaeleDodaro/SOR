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
        $nome=$1 if($line =~m/(?i)Name:\s+(\S+)\n/);
        $nomeVmRSS{$nome}=$1 if($line =~m/(?i)VmRSS:\s+(\d+)/);
    }
    close $fh or die $!;
}
foreach(sort{$nomeVmRSS{$b}<=> $nomeVmRSS{$a} or $a cmp $b} keys %nomeVmRSS);
{
    print "$_ --> $nomeVmRSS{$_}";
}
qx(top -n1);