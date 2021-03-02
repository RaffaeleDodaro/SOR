#!/usr/bin/perl
$opt= shift or die $!;
$file1=shift or die $!;
$file2=shift or die $!;
die $! if($#ARGV>=0);

if($opt eq "-d")
{
    $riga=0;
    open($fh1,"<",$file1) or die $!;
    open($fh2,"<",$file2) or die $!;
    @arrayfh1=<$fh1>;
    @arrayfh2=<$fh2>;
    close $fh1;
    close $fh2;
    $lunghezzafh1=scalar @arrayfh1 - 1;
    $lunghezzafh2=scalar @arrayfh2 - 1;
    $lunghezzaMaggiore=$lunghezzafh1;
    if($lunghezzafh1 > $lunghezzafh2)
    {
        $lunghezzaMaggiore=$lunghezzafh1;
    }
    else{
        $lunghezzaMaggiore=$lunghezzafh2;
    }
    for($i=0;$i<$lunghezzaMaggiore;$i++)
    {
        if("$arrayfh1[$i]" ne "$arrayfh2[$i]")
        {
            print "Differenze in riga $i\n";
            print "$arrayfh1[$i]\n";
            print "-------------------";
            print "$arrayfh2[$i]\n\n";
        }

        if($lunghezzafh2>$lunghezzafh1)
        {
            print "Differenze in riga $i\n";
            print "<MISSING>\n";
            print "-------------------";
            print "$arrayfh2[$i]\n\n";
        }
        if($lunghezzafh1>$lunghezzafh2)
        {
            print "Differenze in riga $i\n";
            print "$arrayfh2[$i]\n";
            print "-------------------";
            print "<MISSING>\n\n";
        }
    }
}
elsif($opt eq "-s")
{
    %array;
    open($fh1,"<",$file1) or die $!;
    open($fh2,"<",$file2) or die $!;
    @arrayfh1=split(" ",$fh1);
    foreach(@arrayfh1)
    {
        $array{$_}=0;
    }
    @arrayfh2=split(" ",$fh2);
    close $fh1;
    close $fh2;

    $lunghezzafh2=scalar @arrayfh2 - 1;

    for($i=0;$i<$lunghezzafh1;$i++)
    {
        for($j=0;$j<$lunghezzafh2;$j++)
        {
            if($arrayfh1[$i] eq $arrayfh2[$j])
            {
                $array{$arrayfh1[$i]}+=1;
            }
            
        }
    }
    @sorted=sort{($array{$b}<=>$array{$a}) or ($a cmp $b)} keys %array;
    foreach(@sorted)
    {
        print "$_ --> $array{$_}\n";
    }
}