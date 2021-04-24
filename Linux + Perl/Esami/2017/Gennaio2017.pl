#!/usr/bin/perl
$output;
foreach(qx{env})
{
    $output= $1 if(m/PATH=(\N+)/)
}
@splitted=split(':',$output);
$dimTotale=0;
foreach(@splitted)
{
    $s=0;
    foreach(qx{ls -l $_ 2>&1}){
        $s+=$1 if(m/\S+\s\d\s\S+\s+\S+\s+(\d+)/)
    }
    print "$_ : $s bytes\n";
    $dimTotale+=$s;
}
print "TOTALE : $dimTotale bytes\n";