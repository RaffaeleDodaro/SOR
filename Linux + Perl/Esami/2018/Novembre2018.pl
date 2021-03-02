#!/usr/bin/perl
die $! if($#ARGV<0);
die $! if($#ARGV>2);
$exe=shift or die $!;
if($exe eq "-r"){
    die $! if($#ARGV>=0);
    @comando=`lsof`;

    $process = shift or die $!;
    open($fh,">","lsof.out");
    print $fh @comando if($process eq "-1");
    if($process ne "-1"){
        foreach(@comando)
        {
            print $fh "$_\n" if(m/$process\s+\d+\s+\w+/);
        }
    }
    close $fh;
}
elsif($exe eq "-b")
{
    die $! if($#ARGV<2);
    $process = shift or die $!;
    $backup = shift or die $!;
    open($fh,"<",$backup) or die $!;
    if($process eq "-1"){
        %hash;
        while(<$fh>)
        {
            if(m/(\w+)\s+\d+\w+\s+\w+\s+\w+\s+\d+\,\d+\s+(\d+)\s+/)
            {
                $hash{$1}+=$2;
            }
        }
        
        foreach(sort{ $hash{$a}<=> $hash{$b}} keys %hash)
        {
            print "$hash{$_} --> $_";
        } 
    }
    else
    {
        $somma=0;
        while(<$fh>)
        {
            if(m/($process)\s+\d+\w+\s+\w+\s+\w+\s+\d+\,\d+\s+(\d+)\s+/)
            {
                $somma+=$2;
            }
        }
        print "$process --> $somma";
    }
    close $fh; 
}