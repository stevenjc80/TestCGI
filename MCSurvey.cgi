#!/usr/bin/perl -wT
# This cgi script takes the responses to a multiple-choice survey, and saves
# them to a file in a results directory on the server.
# Written by Steven Castellucci, Copyright 2018.

use CGI qw(:all);
use CGI::Carp qw(fatalsToBrowser);
use strict;


# Modify the results directory, as appropriate.
my $resultsDir = './results';


# The name of the user's directory (with the response file) will be the first
# defined scalar from the following options: the username authenticated by
# .htaccess, the remote user's IP address, or the local user's name (if running
# the script from the command-line).
my $name = secure($ENV{REMOTE_USER} or $ENV{REMOTE_ADDR} or $ENV{LOGNAME});


print "Content-Type: text/html\n\n"; # Very important! :-)
print "<!DOCTYPE html>\n<html>\n<head><title>Survey Responses</title></head>\n<body>\n";
unless(defined $name) { # Unable to determine user's identity.
    dieNice("Secure login required! Please authenticate and try again.");
} 
unless((-e $resultsDir or mkdir($resultsDir)) and chmod(0770, $resultsDir)) {
    dieNice("Unable to create results directory: $resultsDir");
}
unless((-e "$resultsDir/$name" or mkdir("$resultsDir/$name")) and chmod(0770, "$resultsDir/$name")) {
    dieNice("Unable to create submission directory: $name");
}

# Write responses to file.
my $fh;
unless(open($fh, '>', "$resultsDir/$name/submit.txt") and chmod(0660, $fh)) {
    dieNice("Unable to record responses!");
}
my $q = new CGI;
my $fileOutput = "{";
my $htmlOutput = "";
foreach my $key ($q->param()) {
    my $value = param($key);
    $fileOutput .= "\'$key\': \'$value\', ";
    $htmlOutput .= "<p>$key: $value</p>\n";
}
$fileOutput = substr($fileOutput, 0, -2) . "}\n"; # removes trailing comma and space
print {$fh} $fileOutput;
close($fh);

# Echo the survey responses.
print "<h2>Your submitted answers:</h2>\n";
print "$htmlOutput";
print "</body>\n</html>\n";

# Removes insecure characters in the username.
sub secure {
    my $result = $_[0];
    chomp($result);
    if ($result =~ /^(\w+)\z/) {
        $result = $1;  # Extracted result is considered safe.
    } else {
        dieNice("Disallowed characters in filename: $result");
    }
    return $result;
}

# Print error message to the browser.
sub dieNice {
    my $errmsg = $_[0];
    print "<h2>Error</h2>\n";
    print "<p>ERROR SUBMITTING TEST: DO NOT CLOSE THE WEB BROWSER!</p>\n";
    print "<p>Please inform the teaching assistant</p>\n";
    print "<p>Exception error message:</p>\n";
    print "<p>$errmsg</p>\n";
    print "</body>\n</html>\n";
    exit;
}
