#!/usr/bin/perl
$dir=shift or die $!;
$opt="";
$opt=shift or die $! if($#ARGV>=0);
die $! if($#ARGV>=0);
@output=qx(stat $dir);
$dimMin=10000000000;
$dimMax=0;
$nomeDimMin;
$nomeDimMax;
$sommaDim=0;
$sommaBlocchi=0;
if($opt eq "")
{    
    foreach(@output)
    {
        if(m/\s+File:\s+(.+)\n\s+Size: (\d+)\s+Blocks:\s+(\d+)\s+/)
        {
            $sommaBlocchi+=$3;
            $sommaDim+=$2;
            if($2>$dimMax)
            {
                $dimMax=$2;
                $nomeDimMax=$1;
            }
            if($2<$dimMin)
            {
                $dimMin=$2;
                $nomeDimMin=$1;
            }
        }
    }
    print "sommablocchi: $sommaBlocchi\nsommadim: $sommaDim\nnomeFileMin: $nomeDimMin\nDimMin: $dimMin\nnomeFileMax: $nomeDimMax \ndimMax: $dimMax\n";
}
elsif ($opt eq "-b") {
    $blocchiMin=100000000000;
    $blocchiMax=0;
    $nomeBloccoMin;
    $nomeBloccoMax;
    foreach(@output)
    {
        if(m/\s+File:\s+(.+)\n\s+Size: (\d+)\s+Blocks:\s+(\d+)\s+/)
        {
            $sommaBlocchi+=$3;
            if($3>$blocchiMax)
            {
                $blocchiMax=$3;
                $nomeBloccoMax=$1;
            }
            if($3<$blocchiMin)
            {
                $blocchiMin=$3;
                $nomeBloccoMin=$1;
            }
        }
    }
    print "blocchimin: $blocchiMin\nnomeBlocchiMax: $blocchiMax\nnomeBloccoMin: $nomeBloccoMin\nnomeBloccoMax: $nomeBloccoMax\n";
}
elsif ($opt =~ m/-t=(\N+)/) {
    $tipo=$1;
    foreach(@output)
    {
        if(m/\s+File:\s+(.+)\n\s+Size: (\d+)\s+Blocks:\s+(\d+)\s+IO Block:\s+\d+\s+($tipo)/)
        {
            $sommaBlocchi+=$3;
            $sommaDim+=$2;
            if($2>$dimMax)
            {
                $dimMax=$2;
                $nomeDimMax=$1;
            }
            if($2<$dimMin)
            {
                $dimMin=$2;
                $nomeDimMin=$1;
            }
        }
    }
    print "sommablocchi: $sommaBlocchi\nsommadim: $sommaDim\nnomeFileMin: $nomeDimMin\nDimMin: $dimMin\nnomeFileMax: $nomeDimMax \ndimMax: $dimMax\n";
}
else{
    die $!;
}