#!/usr/bin/perl
die $! if($#ARGV<0 or $#ARGV>1);
$risorsa = shift or die $!;
die $! if($risorsa ne "-c" or $risorsa ne "-m");
$utente = shift or die $!;
%hash;
foreach (qx{top -n1 -b}) {
    if (m/\d+\s+(\S+)\s+\d+\s+\d+\s+\d+\s+\d+\s+\w\s+(\d+,\d+)\s+(\d+,\d+)/) {
        $hash{$1} += $2 if ($risorsa =~ m/-c/);
        $hash{$1} += $3 if ($risorsa =~ m/-m/);
    }
}
open($fh, ">", "stat.log") or die $!;
print $fh "utente $utente CPU: $hash{$utente}\n" if ($risorsa =~ m/-c/);
print $fh "utente $utente MEM: $hash{$utente}\n" if ($risorsa =~ m/-m/);
foreach (sort {$hash{$b} <=> $hash{$a}} keys %hash) {
    print $fh "Max uso CPU: $utente $hash{$utente}%\n" if ($risorsa =~ m/-c/);
    print $fh "Max uso MEM: $utente $hash{$utente}%\n" if ($risorsa =~ m/-m/);
    print $fh "$hash{$_}\n";
    last;
}
close $fh;