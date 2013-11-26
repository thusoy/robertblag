module.exports = function(grunt) {

  // load grunt tasks from package.json
  require('load-grunt-tasks')(grunt);

  // Project configuration.
  grunt.initConfig({

    clean: {
      dist: [
        'dist',
        'robert/**/*.pyc',
      ]
    },

    compass: {
      dist: {
        options: {
          sassDir: 'robert/static/sass/',
          cssDir: 'robert/static/css/',
          outputStyle: 'compressed',
        }
      }
    },

    concurrent: {
      server: {
        options: {
          logConcurrentOutput: true,
        },
        tasks: ['watch', 'shell:devserver']
      }
    },

    shell: {
      options: {
        stdout: true,
        stderr: true,
      },
      devserver: {
        command: 'python run_devserver.py',
      },
      freeze: {
        command: 'python freeze.py',
      }
    },

    watch: {
      options: {
        livereload: true,
      },
      python: {
        files: ['robert/**/*.py'],
        tasks: []
      },
      sass: {
        files: ['robert/static/sass/*.scss'],
        tasks: ['compass'],
      },
      templates: {
        files: ['robert/templates/*.html'],
        tasks: [],
      },
      articles: {
        files: ['articles/*.md'],
        tasks: [],
      },
    },
  });

  grunt.registerTask('default', [
    'build',
    'concurrent:server',
  ]);

  grunt.registerTask('build', [
    'clean',
    'compass',
    'shell:freeze',
  ]);
};
