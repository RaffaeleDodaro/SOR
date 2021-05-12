#!/usr/bin/perl
die $! if ($#ARGV < 0 or $#ARGV > 2);
$file = shift or die $!;
$ip = shift or die $!;
$porta = shift or die $!;
die $! if ($#ARGV >= 0);
open(my $fh, "<", $file) or die $!;
%array;
while (<$fh>) {$array{$1} += 1 if (m/IP\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).(\d+)\s>\s$ip\.$porta/);}
close $fh;
open(my $fh, ">", "output.log") or die $!;
foreach (sort {$array{$b} <=> $array{$a}} keys %array) {print $fh "$_>$ip.$porta --> $array{$_}\n";}
close $fh;