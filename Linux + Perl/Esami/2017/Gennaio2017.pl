#!/usr/bin/perl
$output;
foreach(qx{env})
{
    if(m/PATH=(\N+)/)
    {
        $output= $1;
        last;
    }
}
@splitted=split(':',$output);
$dimTotale=0;
# print "@splitted\n";
foreach(@splitted)
{
    $s=0;
    #print "$_\n";
    @dim = qx{ls -l $_ 2>&1};
    foreach(@dim){
        if(m/\S+\s\d\s\S+\s+\S+\s+(\d+)/)#\S+\s\d\s.+?\s+.+?\s+(\d+)
        {
            $dimTotale+=$1;
            $s+=$1;
        }
    }
    print "$_ : $s bytes\n";
}
print "TOTALE : $dimTotale bytes\n";
