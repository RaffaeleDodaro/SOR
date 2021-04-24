#!/usr/bin/perl
@output=qx{cat ./auth.log};
%hash;
%tent;
foreach(@output)
{
   if(m/Failed password for invalid user (\S+) from ((\d{1,3}\.){3}\d{1,3})/){
       $hash{$2}+=1;
       $tent{$1}+=1;
    }
}
foreach(keys %hash)
{print "$_ --> $hash{$_}\n";}

open(my $fh,">","nuovo.txt") or die $!;

foreach(keys %tent)
{print $fh "$_\n";}

close $fh or die $!;