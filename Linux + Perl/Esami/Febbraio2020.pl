#!/usr/bin/perl

$option     = shift or die "Insert at least one option !";
$rootFolder = shift or die "Insert the root folder !";

@files = qx{find $rootFolder -type f -print};

if ( $option eq "-r" ) {
    $regex = shift or die "Insert the regex for renaming !";
    die "Not a valid regex $regex !" if ( not( $regex =~ m/\/.*\/.*\// ) );
    die "Too much arguments !" if ( scalar @ARGV > 0 );
    if ( $regex =~ m/\/(.*)\/(.*)\// ) {
        $substr      = $1;
        $replaceWith = $2;
    }

    for (@files) {
        chomp;
        $currentFile = $_;
        if ( $currentFile =~ m/$substr/ ) {
            $currentFile =~ s/$substr/$replaceWith/g;
            qx{mv $_ $currentFile};
        }
    }
    print `tree $rootFolder`;
}
elsif ( $option eq "-c" ) {
    die "Too much arguments !" if ( scalar @ARGV > 0 );
    %hash;
    for (@files) {
        chomp;
        if ($_ =~ /.*\.(\w{3})\.srt/) {
            $hash{$1} += 1;
        }
    }

    open($file_out, ">", "count_sorted.txt") or die "$!";
    for (sort{$hash{$b} <=> $hash{$a} or $a cmp $b} keys %hash) {
        print $file_out "$_ --> $hash{$_}\n";
        print "$_ --> $hash{$_}\n";
    }
    close $file_out or die $!;
}
else {
    die "Not a valid option $option !";
}

