import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

void main(List<String> args) async {
  String backendUrl = "http://localhost:8085";

  if (args.isNotEmpty) {
    backendUrl = args[0];
  }
  await setupDesktop();
  runApp(DjangoApp(backendUrl));
}

class DjangoApp extends StatelessWidget {
  final String backendUrl;

  const DjangoApp(this.backendUrl, {super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Green Cloud Demo',
      home: FletApp(pageUrl: "http://localhost:8085"),
    );
  }
}
