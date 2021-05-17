#!/usr/bin/perl
die $! if ($#ARGV < 0 or $#ARGV > 2);
$nome = shift or die $!;
$s = shift or die $!;
$f = shift or die $!;
die $! if ($f > 23 or $s > $f);
@output = qx{cat $nome};
$sommaUDP = 0;
$sommaNOUDP = 0;
open(my $fh, ">>", "udp.log") or die $!;
@array;
foreach (@output) {
    $r = $_;
    if (m/(\d+)(\:\d+\:\d+\.\d+) IP (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\.(\d+) > (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\.(\d+)\: (\w+)/) {
        $t = $7;
        $stringa = "$1$2 --> $3.$4 > $5.$6\n";
        if ($1 >= $S and $1 <= $f) {
            if ($t =~ m/UDP/) {
                print $fh "$stringa";
                $sommaUDP += 1;
            }
            else {
                push @array, $stringa;
                $sommaNOUDP += 1;
            }
        }
    }
}

print $fh "Totale: $sommaUDP\n";
close $fh;
open(my $fh2, ">", "flags.log") or die $!;
print $fh2 reverse @array;
print $fh2 "Totale: $sommaNOUDP\n";
close $fh2;