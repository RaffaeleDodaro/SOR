#!/usr/bin/perl
die $! if($#ARGV<1);
$scommesse=shift or die $!;
$partite=shift or die $!;
open($fh,">","check.txt");
open($fScommesse,"<",$scommesse);
open($fPartite,"<",$partite);

while(<$fScommesse>)
{
     if (m/^#Schedina/) {
            print $fh $_;
            $moltiplicatore = 1.0;
            $vincita="OK";
            $possibileVincita=0;
            next;
        }   
    
    if(m/(\w+\-\w+)\s+(\w*)\s+(\d+\.\d+)/)
    {
        $partita=$1;
        $segno=$2;
        $quota=$3;
        push @quote, $3;
        
        while(<$fPartite>)
        {
            if(m/$partita\s+(\d+)\-(\d+)/)
            {
                if($1>$2 && $segno eq "1")
                {
                    print $fh "$partita     $segno     $quota --> OK";
                }
                elsif($1<$2 && $segno eq "2")
                {
                    print $fh "$partita     $segno     $quota --> OK";
                }
                elsif($1 eq $2 && $segno eq "X")
                {
                    print $fh "$partita     $segno     $quota --> OK";
                }
                else
                {
                    print $fh "$partita     $segno     $quota --> NO";
                    $vincita="NO";
                }
            }
        }
        
    }
    if (m/^#Importo Scommesso\s+(\d+)$/) {
        foreach(@quote)
        {
            $moltiplicatore=$moltiplicatore*$_;
        }
        $possibileVincita=$moltiplicatore*$1;
        print $fh "#importo scommesso $1\n #Moltiplicatore: $moltiplicatore\n#Possibile Vincita: $possibileVincita\n#Vincita: $vincita";
    }
}

close $fh;
close $fScommesse;
close $fPartite;