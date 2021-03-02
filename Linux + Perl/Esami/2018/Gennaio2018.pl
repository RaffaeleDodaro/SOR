#!/usr/bin/perl
$path = shift or die $!;
$s=shift or die $!;
$f=shift or die $!;
die "f<s" if($f<$s);
open(my $fh,"<",$path);
@filtrati;
while (my $line=<$fh>) {
    chomp $_;
    if($line=~m/(.+)\s+IP\s+(\d+.\d+.\d+.\d+.\d+)\s+>\s+(\d+.\d+.\d+.\d+.\d+):\s+(\w+)/)
    {
        if($1>=$s && $1<=$f)
        {
            push @filtrati, $line;
        }
    }
}
close $fh;
open($udp,">","udp.log");
$s=0;
foreach(@filtrati)
{
    chomp;
    $copia=$_;
    $copia=~m/(.+)\s+IP\s+(\d+.\d+.\d+.\d+.\d+)\s+>\s+(\d+.\d+.\d+.\d+.\d+):\s+(\w+)/;
    print $udp "$1 --> $2 > $3\n";
    $s+=1;
}
print $udp "Totale: $s\n";
close $udp;
@sorted=sort{$b cmp $a}@filtrati;
open($flags,">","flags.log");
$s=0;
foreach(@sorted)
{
    chomp;
    $copia=$_;
    $copia=~m/(.+)\s+IP\s+(\d+.\d+.\d+.\d+.\d+)\s+>\s+(\d+.\d+.\d+.\d+.\d+):\s+(\w+)/;
    if($4 ne "UDP")
    {
        print $flags "$1 --> $2 > $3\n";
        $s+=1;
    }
}
print $flags "Totale: $s\n";
close $flags;













##############################
#       versione prof        #
##############################
#!/usr/bin/perl

########### ESEGUO I CONTROLLI PIÃ™ BANALI SUGLI ARGOMENTI IN INPUT ############
die "Too much parameters in input !" if ($#ARGV > 2);
my $dump_filename = shift || die "Few parameters in input !";
my $start = shift || die "Few parameters in input !";
my $end = shift || die "Few parameters in input !";

die "Parameters start and end are not valid !" if ($start < 0 || $start > $end || $end >= 24);

########### INIZIALIZZO LE STRUTTURE DATI ############
my %udp;
my %flags;

########### LEGGO IL FILE DUMP.LOG E CONTROLLO LE RIGHE ############
open(my $dump, "<", $dump_filename) || die "Cannot open file $dump_filename !";
$c=0;
while(<$dump>)
{
  chomp $_;
  if ($_ =~ m/(.*)\sIP\s((?:\d{1,3}\.){3}\d{1,3}(?:\.\d*){0,1})\s>\s((?:\d{1,3}\.){3}\d{1,3}(?:\.\d*){0,1}):\s(\w*)[\s\,\+].*/)
  {
    if ((substr $1, 0, 2) >= $start && (substr $1, 0, 2) <= $end)
    {
    	####### $4 Ã¨ il tipo di pacchetto --- non era richiesto stamparlo ####### 
      if ($4 eq "UDP") { $udp{$1} = "$1 --> $2 > $3 ### $4"; }
      else { $flags{$1} = "$1 --> $2 > $3 ### $4"; }
    }
  }
}
###### IL FILE RIMANE APERTO GIUSTO IL TEMPO NECESSARIO AD ESEGUIRE LE OPERAZIONI ######
close $dump || die "Cannot close file $dump_filename";

########### SCRIVO SU FILE UDP.LOG ORDINATAMENTE ############
open(my $udp_fh, ">", "udp.log") || die "Cannot open file udp.log !";
# Attenzione al tipo di dato della chiave dell'hash. Se nel timestamp sono rimasti i caratteri come ":" e "." allora si tratta di una stringa
# In questo caso particolare Ã¨ possibile evitare di rimuovere questi caratteri per effettuare l'ordinamento
print $udp_fh "$udp{$_} \n" for (sort{$a cmp $b} keys %udp);  
print $udp_fh "Totale: ", scalar keys %udp;
close $udp_fh || die "Cannot close file udp.log";

########### SCRIVO SU FILE FLAGS.LOG ORDINATAMENTE ############
open(my $flags_fh, ">", "flags.log") || die "Cannot open file flags.log !";
print $flags_fh "$flags{$_} \n" for (sort{$b cmp $a} keys %flags);
print $flags_fh "Totale: ", scalar keys %flags;
close $flags_fh || die "Cannot close file udp.log";