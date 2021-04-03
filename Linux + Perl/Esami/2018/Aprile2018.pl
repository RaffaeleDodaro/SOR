#!/usr/bin/perl
$history_file=shift or die $!;
$opt=".";
$opt=shift or die $! if($#ARGV>=0);
$find=shift or die $! if($#ARGV>=0);
die $! if($#ARGV>=0);
@output=qx(cat $history_file);
print "@output" if($opt eq ".");
if($opt =~ m/--sort/)
{
    @sorted=sort @output;
    print "@sorted";
}
elsif($opt =~ m/--stat/)
{
    %hash;
    foreach(@output)
    {
        if(m/\d+\s+(\S+).+/)
        {
            $hash{$1}+=1;
        }
    }
    foreach(keys %hash)
    {
        print "$_ --> $hash{$_}\n";
    }
}
elsif($opt =~ m/-f/)
{
    
    foreach(@output)
    {
        $tutta=$_;
        if(m/($find).+/)
        {
            print "$tutta";
        }
    }
}