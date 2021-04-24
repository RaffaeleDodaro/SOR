#!/usr/bin/perl
die $! if($#ARGV>2);
$file=shift or die $!;
@output=qx{cat $file};
$opzione="";
$opzione=shift or die $! if($#ARGV>=0);
print "@output" if($opzione eq "");
if($opzione eq "--sort"){
    @sorted=sort @output;
    print "@sorted";
}
elsif($opzione eq "--stat"){
    %hash;
    foreach(@output)
    {
        $hash{$1}+=1 if(m/(\S+)\s.+/)
    }
    foreach(keys %hash)
    {
        print "$_ --> $hash{$_}\n";
    }
}
elsif($opzione eq "-f"){
    $arg=shift or die $! if($#ARGV>=0);
    foreach(@output)
    {
        print "$_\n" if(m/(^$arg)\s/);
    }
}
else{die $!;}